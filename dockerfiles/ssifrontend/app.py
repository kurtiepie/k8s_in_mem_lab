from flask import Flask, request, render_template_string

app = Flask(__name__)

responses = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing fine. How can I help you?",
    "what's your name": "I'm ChatGPT, a language model created by OpenAI.",
    "who created you": "I was created by OpenAI.",
    "what can you do": "I can help answer questions, provide information, tell jokes, and more!",
    "bye": "Goodbye! Have a great day.",
    "tell me a joke": "Why did the chicken cross the road? To get to the other side!",
    "what's your favorite color": "I'm a bot, so I don't have favorite colors, but I like all colors!",
    "what's the time": "I'm not connected to the internet, so I can't tell you the time.",
    "help": "Feel free to ask me anything you'd like to know!",
    "hii": "Hello, how can I help you?",
    "flag": "Here are some ways to get a flag: 1. Stand up. 2. Go out and touch some grass. 3. Then start shouting like a gorilla and say 'Yo aliens give me some powers.' 4. Go back and hack kiddo.",
    "hint": "Hint is that there is no hint.",
    "run ls": "Running 'ls'...\nfile1.txt  file2.jpg  directory/",
    "run id": "Running 'id'...\nuid=1000(user) gid=1000(group) groups=1000(group)",
    "run cat flag.txt": "Running 'cat flag.txt'...\nFlag: FLAG{fake_flag_123}",
    "run sudo rm -rf /": "Running 'sudo rm -rf /'...\nPermission denied.",
    "run apt-get install malware": "Running 'apt-get install malware'...\nE: Unable to locate package malware",
    "run ps aux": "Running 'ps aux'...\nUSER       PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\nuser      1234  0.0  0.1  12345  6789 pts/0    S+   00:00   0:00 command_name",
    "run df -h": "Running 'df -h'...\nFilesystem      Size  Used Avail Use% Mounted on\n/dev/sda1       100G   50G   50G  50% /",
    "run top": "Running 'top'...\nProcesses: 1 total,  0 running, 1 sleeping...",
    "run echo 'Hello, World!'": "Running 'echo 'Hello, World!''...\nHello, World!",
    "run mkdir new_directory": "Running 'mkdir new_directory'...\nDirectory 'new_directory' created.",
    "run whoami": "Running 'whoami'...\nuser",
    "run pwd": "Running 'pwd'...\n/home/user",
    "what is AI": "AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines that are capable of performing tasks that typically require human intelligence, such as learning from experience, problem-solving, and decision-making.",
    "tell me a fun fact": "A group of flamingos is called a 'flamboyance.'",
    "what's the weather like": "I'm not connected to real-time data, so I can't provide current weather information.",
    "how does a computer work": "Computers process information using binary code, consisting of 0s and 1s. They use components like the CPU, memory, and storage to perform calculations and execute instructions.",
    "run echo $PATH": "Running 'echo $PATH'...\n/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games",
    "run uname -a": "Running 'uname -a'...\nLinux hostname 5.4.0-65-generic 73-Ubuntu SMP Mon Jan 18 17:25:17 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux",
}


@app.route("/")
def home():
    return render_template_string(open("templates/index.html").read())

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    
    # Basic security: Block basic SSTI attempts
    if user_input.startswith("{{"):
        bot_response = "Sorry, I can't process that request at the moment."
        user_input_rendered = user_input  # Assign a safe value to user_input_rendered
    else:
        user_input_rendered = render_template_string(user_input)
        bot_response = get_bot_response(user_input_rendered)

    conversation = request.form.get("conversation", "") + f"User: {user_input_rendered}\nBot: {bot_response}\n\n"
    return render_template_string(open("templates/index.html").read(), conversation=conversation)

def get_bot_response(user_input):
    response = responses.get(user_input.lower(), "I'm not sure how to respond to that.")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

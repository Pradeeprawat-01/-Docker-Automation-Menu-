import subprocess
import os

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"{RED}❌ Error while executing: {command}{RESET}")

while True:
    clear_screen()
    print(f"""{CYAN}
╔═════════════════════════════════════════════╗
║           🚀 Docker Automation Menu         ║
╠═════════════════════════════════════════════╣
║ 1. 📥 Pull an Image                         ║
║ 2. 🖥️  Run an Image (Interactive Mode)       ║
║ 3. 👻 Run an Image (Detached Mode)          ║
║ 4. ▶️  Start a Container                    ║
║ 5. 🔌 Attach to a Container                 ║
║ 6. ⏹️  Stop a Container                     ║
║ 7. 📦 Show All Containers                   ║
║ 8. 🖼️  Show All Images                      ║
║ 9. 🚚 Show Running Containers               ║
║10. 🗑️  Delete a Container                   ║
║11. 🧹 Delete an Image                       ║
║12. 🗑️  Delete ALL Containers                ║
║13. ❎ Exit                                   ║
╚═════════════════════════════════════════════╝
{RESET}""")

    choice = input(f"{YELLOW}🔸 Enter your choice: {RESET}")

    if choice == '1':
        image = input("🔹 Enter image name (e.g., ubuntu:latest): ")
        run_command(f"docker pull {image}")
        print(f"{GREEN}✅ Pulled image '{image}' successfully.{RESET}")

    elif choice == '2':
        image = input("🔹 Enter image name to run interactively: ")
        name = input("🔹 Enter a name for the container (optional): ")
        name_option = f"--name {name}" if name else ""
        run_command(f"docker run -it {name_option} {image}")

    elif choice == '3':
        image = input("🔹 Enter image name to run in detached mode: ")
        name = input("🔹 Enter a name for the container (optional): ")
        name_option = f"--name {name}" if name else ""
        run_command(f"docker run -d {name_option} {image}")
        print(f"{GREEN}✅ Running '{image}' in detached mode.{RESET}")

    elif choice == '4':
        cid = input("🔹 Enter container ID or name to start: ")
        run_command(f"docker start {cid}")
        print(f"{GREEN}✅ Container '{cid}' started.{RESET}")

    elif choice == '5':
        cid = input("🔹 Enter container ID or name to attach: ")
        run_command(f"docker attach {cid}")

    elif choice == '6':
        cid = input("🔹 Enter container ID or name to stop: ")
        run_command(f"docker stop {cid}")
        print(f"{GREEN}✅ Container '{cid}' stopped.{RESET}")

    elif choice == '7':
        print(f"{MAGENTA}📦 All Containers:{RESET}")
        run_command("docker ps -a")

    elif choice == '8':
        print(f"{MAGENTA}🖼️ All Images:{RESET}")
        run_command("docker images")

    elif choice == '9':
        print(f"{MAGENTA}🚚 Running Containers:{RESET}")
        run_command("docker ps")

    elif choice == '10':
        cid = input("🔹 Enter container ID or name to delete: ")
        run_command(f"docker rm -f {cid}")
        print(f"{GREEN}🗑️ Container '{cid}' deleted.{RESET}")

    elif choice == '11':
        img = input("🔹 Enter image ID or name to delete: ")
        run_command(f"docker rmi  {img}")
        print(f"{GREEN}🧹 Image '{img}' deleted.{RESET}")

    elif choice == '12':
        confirm = input(f"{RED}⚠️  Are you sure you want to delete ALL containers? (yes/no): {RESET}")
        if confirm.lower() == "yes":
            run_command("docker rm $(docker ps -a -q)")
            print(f"{GREEN}✅ All containers deleted.{RESET}")
        else:
            print(f"{YELLOW}⏳ Deletion cancelled.{RESET}")

    elif choice == '13':
        print(f"{CYAN}👋 Exiting. Have a great day!{RESET}")
        break

    else:
        print(f"{RED}❗ Invalid choice. Try again.{RESET}")

    input(f"\n{YELLOW}🔁 Press Enter to continue...{RESET}")


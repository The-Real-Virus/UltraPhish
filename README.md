# 🎣 UltraPhish 🎣

## 📜Description  
UltraPhish is a powerful tool designed for ethical hacking and cybersecurity research.  
It provides a user-friendly interface to deploy phishing pages securely using multiple tunneling services.  

⚠️ Disclaimer: This tool is intended for educational purposes and authorized penetration testing only.  
Do not use it for illegal activities.  

## 🔑Features
✅ Multi-Tunneling Support: Use Cloudflared, LocalXpose, Serveo, and Ngrok for secure phishing.  
✅ Auto Installation: Automatically installs missing dependencies.  
✅ OTP Support: Capture one-time passwords (OTP) if required.  
✅ URL Masking: Generate a phishing link with a custom mask.  
✅ Credential Capture: Stores login credentials and IP addresses of victims.  
✅ Custom Templates: Includes multiple phishing page templates.  
✅ Automated Ngrok Setup: Installs, authenticates, and fetches Ngrok tunnels seamlessly.  
✅ Cross-Platform: Works on Linux, Termux, and Windows (via WSL).  

- Multi platform (Supports most linux)  
- Easy to use  
- Possible error diagnoser  
- 70+ Website templates   
- Upto 6 links for phishing  
- Argument support  
- Credentials mailing  
- Custom masking of URL  
- URL Shadowing  
- Redirection URL settings  
- Portable file (Can be run from any directory)  
- Get IP Address and many other details along with login credentials  

## 🚀Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  
>sudo apt upgrade  

Step 2: Clone the repository  
>git clone https://github.com/The-Real-Virus/UltraPhish.git  

Step 3: Install dependencies (git, python, php ssh)  
>For Debian (Ubuntu, Kali-Linux, Parrot)  
    - ```sudo apt install git python3 php openssh-client -y```  
>For Arch (Manjaro)  
    - ```sudo pacman -S git python3 php openssh --noconfirm```  
>For Redhat(Fedora)  
    - ```sudo dnf install git python3 php openssh -y```  
>For Termux  
    - ```pkg install git python3 php openssh -y```  

Step 4: Install all modules(MUST BEFORE RUNNING SCRIPT)  
>1) `sudo apt install python3-bs4`  
>2) `sudo apt install python3-rich`  
>3) `sudo apt install python3-requests`  
>4) `sudo apt install git python3 php openssh-client -y`  
>5) `git clone https://gitlab.com/The-Real-Virus/ultrasites.git $HOME/.websites`  

Step 5: After Completing the process (Runing Step 4 all 5 commands), now u can run script  
>python3 ultraphish.py  

## ⚙️Troubleshooting

- Some secured browsers like Firefox can warn for '@' prefixed links. You should use pure links or custom link to avoid it.  
- Termux from play store in not supported. Download termux from fdroid or github  
- VPN or proxy prevents tunneling and even proper internet access. Turn them off you have issues.  
- Some android requires hotspot to start Cloudflared and Loclx. If you face 'tunneling failed' in android,  
  most probably your hotspot is turned off. Turn it on and keep it on untill you close PyPhisher.  
- If you want mailing credentials then you need to use app password.  
  Visit [here](https://myaccount.google.com/u/0/apppasswords) and generate an app password, put that in `files/email.json`. You may need to enable 2FA before it.  
- Ensure Cloudflared/LocalXpose/Serveo is installed.  
- Restart your terminal and re-run the script.  
- Run the script as root (sudo ./ultraphish.py).  

## 💡Tips & Support !
1) Always test Ngrok manually before using it in the script.  
2) Use a VPN for extra security when testing phishing pages.  
3) Use in a legal environment (e.g., testing your own systems).  
4) Disable unwanted tunnelers in the script if not needed.  
5) Use cloudflared and Serveo Links.  
6) Use grabify ip logger or other url shortner to Manually Mask the url.  
7) must test link on ur device before sending.  
8) if cloudflared down then use serveo.  

          OS       | Support Level
        -----------|--------------  
        Linux      | Excellent (100% Working & Recommended)  
        Android    | Not Tested  
        iPhone     | Alpha (Recommended docker)  
        MacOS      | Alpha (Recommended docker)  
        Windows    | Unsupported (Use docker/virtual-box/vmware)  
        BSD        | Never tested  

## 🤝Follow the Prompts !
1. Run the script  
2. Choose a Website  
3. Wait sometimes for setting up all  
4. Send the generated link to victim  
5. Wait for victim login. As soon as he/she logs in, credentials will be captured  

## 🛠️Requirements


 - `Python(3)`
   - `requests`
   - `rich`
 - `PHP`
 - `SSH`
 - 900MB storage
 
If not found, php and python modoules will be installed on first run

## 📂Example OutPut
	[•] Initializing PHP server at localhost:8080....

	[+] PHP Server has started successfully!

	[•] Initializing tunnelers at the same address.....

	[+] Starting Ngrok Tunnel...
	[DEBUG] Extracted Ngrok URL: https://abc123.ngrok.io

	[+] Your URLs are given below:

	╭─ CloudFlared ─────────────────────────────────────────────╮
	│ URL : https://test-cloudflare.trycloudflare.com          │
	╰──────────────────────────────────────────────────────────╯

	╭─ Ngrok ───────────────────────────────────────────────╮
	│ URL : https://abc123.ngrok.io                         │
	╰──────────────────────────────────────────────────────╯

	[+] Waiting for login info....Press Ctrl+C to exit


# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.  

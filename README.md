# ChithiStorm
![Preview Image](https://i.ibb.co.com/PGVQKJMD/Screenshot-2025-03-24-00-58-57-420-com-termux-edit.jpg)
## Prerequisites

- **Python 3.x** installed on your system.
- Required Python packages: `httpx`, `colorama`.

## Installation Guide

1. **Clone the Repository:**

   Begin by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/BrainlessDip/ChithiStorm.git
   cd ChithiStorm
   ```

2. **Install Required Dependencies:**

   Install the necessary Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Delay:**

   Modify the `config.json` file to set your preferred delay (in seconds) between message submissions:

   ```json
   {
       "delay": 0.5, // Delay in seconds
       "lastData": "",
       "lastCount": 18
   }
   ```

## How to get data ?
todo

## Usage Instructions

1. **Launch the Script:**

   Execute the script by running the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Follow the On-Screen Prompts:**

   - **Data:** Enter the target Chithi data. If you press Enter without typing, the script will use the last saved data
   - **Message Count:** Specify the number of messages you wish to send. Press Enter to use the last saved count

   The script will automatically save your last-used data and message count for future sessions

## Example Workflow

```bash
[!] Copy the data from network tab

[~] Enter data (N4Igxg9gdgLgprE):
[~] Enter message count (100):
```

## Disclaimer

This tool is designed strictly for educational and testing purposes. Use it responsibly and ensure you have permission from the target user before sending messages. Misuse of this tool is not encouraged and is solely the responsibility of the user
# URL-Shortner

#### Description:
This Python script shortens URLs using the Cutt.ly API. By entering a URL, the script will generate a shorter version using the Cutt.ly service. It ensures the input URL is valid and handles potential errors during the API call. The script requires an API key from Cutt.ly to function properly.

#### Code Explanation:
1. **Importing Requests Module**: 
   - The `requests` module is used to send HTTP requests to the Cutt.ly API and handle the response.

2. **`shorten_url` Function**:
   - This function takes an API key and a URL to shorten, sends a request to the Cutt.ly API, and returns the shortened URL or an error message.
   - If the API call is successful and returns a valid shortened link, it is extracted and returned.
   - If there's any issue with the API or the URL, an error message is displayed.

3. **Main Function**:
   - The main function prompts the user to input a URL and invokes the `shorten_url` function to process the shortening.
   - It also checks if the API key is provided correctly and ensures the URL input is valid.

---

### Usage:

1. **Clone the Repository**:
   Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener
   ```

2. **Install the Requests Library**:
   Ensure that the `requests` library is installed. You can install it using `pip`:

   ```bash
   pip install requests
   ```

3. **Run the Script**:
   Open your terminal or command prompt and run the Python script:

   ```bash
   python url_shortener.py
   ```

4. **Enter the URL**:
   The script will prompt you to enter the URL that you want to shorten:

   ```text
   Enter the URL to shorten: https://www.example.com
   ```

5. **Get Shortened URL**:
   After entering the URL, the script will display the shortened version:

   ```text
   Shortened URL: https://cutt.ly/abc123
   ```

6. **Error Handling**:
   - If an incorrect or empty URL is entered, the script will print an appropriate error message.
   - If the API key is missing or invalid, the script will notify the user.

---

### Screenshot:

1. **Initial Prompt**:
   <img width="358" alt="{E7C0FD47-673B-47DA-8EE2-36E03BCE6C7B}" src="https://github.com/user-attachments/assets/af242ae4-7c42-4c63-aa3a-43643b49f175">


2. **Shortened URL Output**:
   <img width="360" alt="{6F1004DC-6C5D-4286-9546-8FF8557468A1}" src="https://github.com/user-attachments/assets/9050dc21-6543-49fb-9706-5c554fa4a594">


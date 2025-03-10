# YouTube DevShare Tutorials!

This is a community-driven platform where developers share their favorite YouTube programming tutorials.
Contribute your knowledge and discover valuable resources to enhance your coding skills!

## Features

- **Contributor Registration:** A contributor can register with their username and linkedin profile url.
- **Add Tutorials:** Easily add new tutorials with titles, channel names, video url or playlist url, and a brief description.
- **View Tutorials:** Browse a list of all your saved tutorials in a table format.
- **Watch Tutorial:** Watch tutorial directly from the app.
- **Delete Tutorials:** Remove tutorials that you no longer need.
- **Search Tutorials:** Search for specific tutorials by ID.
- **Object Oriented Data:** The application can return database results as python objects.

## Getting Started

### Prerequisites

- Python 3.13.1
- Streamlit v1.43.1
- SQLite3

### Installation

1.  **Clone the repository (or download the code):**

    ```bash
    git clone https://github.com/endang-ismaya/st-devshare-tutorials.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd st-devshare-tutorials
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2.  **Open your web browser:**

    - Streamlit will automatically open a browser window displaying the application. If not, open your browser and navigate to the URL displayed in the terminal.

### Database

- The application uses an SQLite3 database named `youtube_tutorials.db`.
- The database contains a table named `tutorials` with the following columns:
  - `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
  - `title` (TEXT)
  - `channel_name` (TEXT)
  - `video_url` (TEXT)
  - `brief_description` (TEXT)

### Application Structure

The application is structured using a Model-View-Template (MVT) like architecture:

- **models:** A folder contains the database interaction logic (models).
- **views:** A folder contains the application logic (views).
- **templates:** A folder contains the application views or frontend templates.
- **app.py:** The main program file.
- **Tutorial class:** A python class that represents a single tutorial record.
- **TutorialModel class:** A python class that represents a Tutorial Model for method and properties.

### Enhancements

Here are some potential enhancements for this application inthe future:

- **Search Functionality:** Improve search capabilities to include searching by channel or title.
- **Error Handling:** Implement more robust error handling for database operations.
- **Styling:** Improve the app's appearance using Streamlit's styling options.
- **User Authentication:** Add user authentication [permanently] as currently only using session_state.
- **Learning Path Functionality:** Create a collection of videos for a learning path.

### Contributing

Contributions are welcome! If you have any ideas for improvements or find any bugs, please feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License.

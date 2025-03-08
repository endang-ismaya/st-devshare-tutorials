# YouTube Programming Tutorial Tracker

This is a Streamlit application that allows you to track your progress through YouTube programming tutorials. It uses SQLite3 for data storage, providing a simple and efficient way to manage your learning resources.

## Features

- **Add Tutorials:** Easily add new tutorials with titles, channel names, playlist information, and status (To Watch, Watching, Completed).
- **View Tutorials:** Browse a list of all your saved tutorials in a table format.
- **Update Status:** Update the status of tutorials as you progress.
- **Delete Tutorials:** Remove tutorials that you no longer need.
- **Search Tutorials:** Search for specific tutorials by title.
- **Object Oriented Data:** The application can return database results as python objects.

## Getting Started

### Prerequisites

- Python 3.13
- pip (Python package installer)

### Installation

1.  **Clone the repository (or download the code):**

    ```bash
    git clone [repository_url]
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd [project_directory]
    ```

3.  **Install the required packages:**

    ```bash
    pip install streamlit
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
  - `channel` (TEXT)
  - `playlist` (TEXT)
  - `status` (TEXT)

### Application Structure

The application is structured using a Model-View-Template (MVT) like architecture:

- **models:** A folder contains the database interaction logic (models).
- **views:** A folder contains the application logic (views).
- **templates:** A folder contains the application views or frontend templates.
- **app.py:** The main program file.
- **TutorialObject class:** A python class that represents a single tutorial record.

### Enhancements

Here are some potential enhancements for this application inthe future:

- **Search Functionality:** Improve search capabilities to include searching by channel or playlist.
- **Playlist Links:** Add clickable links to YouTube playlists.
- **Detailed View:** Create a detailed view for each tutorial, showing more information.
- **Error Handling:** Implement more robust error handling for database operations.
- **Styling:** Improve the app's appearance using Streamlit's styling options.
- **Video progress:** Add columns for video progress, and current video.
- **Sorting:** Add the ability to sort the table data.
- **User Authentication:** Add user authentication to allow multiple users.
- **Deployment:** Deploy the application to Streamlit Sharing or another hosting platform.

### Contributing

Contributions are welcome! If you have any ideas for improvements or find any bugs, please feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License.

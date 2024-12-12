# Quick Notes Chrome Extension

Quick Notes is a lightweight Chrome extension that allows users to take notes while browsing any website. Whether you're conducting research, jotting down ideas, or saving snippets, Quick Notes makes it easy to stay organized without leaving your browser.

---

## Features

- **Popup Note-Taking**: Quickly open a popup to write and save notes.
- **Persistent Storage**: Notes are saved locally in the browser and remain available after closing Chrome.
- **Highlight & Save**: Highlight text on any webpage and save it as a note.
- **Cloud Sync (Optional)**: Synchronize your notes across devices using Chrome Sync.
- **Modern UI**: Simple and clean design for a seamless experience.

---

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Rugwiroparfait/NoteExtension.git
   ```

2. Navigate to `chrome://extensions/` in your Chrome browser.

3. Enable **Developer mode** in the top-right corner.

4. Click **Load unpacked** and select the project folder.

5. The Quick Notes extension should now be added to your browser.

---

## Usage

1. Click on the Quick Notes icon in your Chrome toolbar to open the popup.
2. Write your note in the provided text area and click "Save Note."
3. Highlight any text on a webpage, and Quick Notes will automatically save it (if content scripts are enabled).
4. Access saved notes anytime from the popup or sync them to your other devices (if enabled).

---

## Project Structure

```
chrome-extension/
│
├── manifest.json       # Metadata and configuration for the extension
├── popup/              # Files related to the popup interface
│   ├── popup.html
│   ├── popup.js
│   ├── popup.css
│
├── background/         # Background scripts for persistent tasks
│   ├── background.js
│
├── content/            # Scripts injected into webpages
│   ├── content.js
│
├── utils/              # Reusable helper functions
│   ├── storage.js
│
├── icons/              # Icons for the extension
│   ├── icon16.png
│   ├── icon48.png
│   ├── icon128.png
│
└── README.md           # Project documentation
```

---

## Development

### Prerequisites
- **Node.js** (Optional): For additional development tooling.
- A text editor (e.g., VS Code).

### Steps
1. Make changes to the extension files (e.g., popup, content, or background scripts).
2. Reload the extension in `chrome://extensions/` after saving changes.

### Adding Dependencies
If your extension grows in complexity, consider using a build tool like **Webpack** or **Vite** for modularization and dependency management.

---

## Future Enhancements

- Add support for exporting notes to a file (e.g., JSON or Markdown).
- Integrate a backend for user authentication and cloud storage.
- Implement advanced text formatting options (e.g., bold, italics).
- Add keyboard shortcuts for quick access.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

For questions or support, please email [rugwiroparfait003@gmail.com](mailto:rugwiroparfait003@gmail.com) or open an issue on GitHub.



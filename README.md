# Static Site Generator (SSG)

A lightweight Python-based tool that transforms Markdown content into a clean, static HTML website. Whether you want to share personal notes, publish a blog, or create simple documentation, this generator takes raw Markdown files and produces attractive, responsive HTML pages along with your chosen layout and styles.

## What Is This?

This is a **Static Site Generator (SSG)** written in Python.  
Its purpose is simple:  
➡️ **You write Markdown files** (`.md`) in the 'content' folder
➡️ The generator **converts them into a complete HTML website** in the 'docs' folder

🔗 **Live Demo Exemple (generated with this tool):**  
[https://thibault-deverge.github.io/SSG_Static-Site-Generator/](https://thibault-deverge.github.io/SSG_Static-Site-Generator/)

## Why Use This SSG?

- **Share Markdown Notes as Web Pages**: Convert meeting notes, project documentation, or personal journals written in Markdown into a shareable HTML page in seconds.
- **Generate Simple Documentation**: Create a documentation website for an open-source project or internal tool by organizing Markdown files into a coherent site structure.
- **Keep It Simple**: No database or server setup—just Markdown, a template, and Python. Ideal for quick publishing and version control.

## Features

- **Markdown to HTML Conversion**: Parses Markdown files into HTML, preserving headings, lists, code blocks, inline formatting, images, and links.
- **Template Injection**: Uses a single HTML template to wrap all pages with consistent header, footer, and CSS styling.
- **Directory Mirroring**: Recursively walks your `content/` folder and writes matching HTML files in the output directory, preserving subfolder hierarchy.
- **Static Asset Copying**: Automatically copies CSS, images, and other static assets from the `static/` directory to the output, so your styles and media appear alongside generated pages.
- **Simple CLI Workflow**: One command to build your entire site and an optional local server to preview changes.

## Quick Start

1. **Prerequisites**

   - Python 3.6 or higher installed on your system.

2. **Project Layout**

   ```
   your-project/
   ├── content/             # Your Markdown files organized in folders
   │   ├── index.md
   │   └── blog/
   │       └── post1.md
   ├── static/              # CSS, images, and other assets
   │   ├── css/style.css
   │   └── images/logo.png
   ├── template.html        # Base HTML template with placeholders
   ├── src/                 # SSG Python source files
   ├── docs/                # Generated output (HTML, CSS, images)
   ├── tests/               # Unit tests for conversion logic
   ├── build.sh             # Builds site into docs/
   ├── main.sh              # Builds site into docs and start local server/
   └── test.sh              # Runs unit tests
   ```

3. **Build the Site**

   ```bash
   ./build.sh
   ```

   - This command clears any existing `docs/` folder, copies all files from `static/` into `docs/`, and converts every Markdown file under `content/` into an HTML page under `docs/`.

   ⚠️ Important if you're deploying with GitHub Pages:
   Make sure the path passed in build.sh matches your repository name if you're using a custom GitHub Pages subfolder.

4. **Preview Locally** (Optional)

   ```bash
   ./main.sh
   ```

   - Starts a simple HTTP server on port 8888, serving the `docs/` folder. Open your browser at [http://localhost:8888](http://localhost:8888).

## How It Works

1. **File Copying**: The `static/` directory is copied verbatim into the `docs/` output directory—stylesheets, images, and fonts are preserved.

2. **Recursive Generation**: The generator walks through each folder in `content/`. For every `.md` file found, it:

   - Reads the Markdown content.
   - Converts it to an HTML fragment (handling headers, lists, code, etc.).
   - Extracts the first-level heading (`# Title`) as the page title.
   - Injects both title and content into `template.html`.
   - Writes the result to a corresponding `.html` file under `docs/`, mirroring the folder structure.

3. **Template Placeholders**:

   - `{{ Title }}` is replaced by the extracted page title.
   - `{{ Content }}` is replaced by the converted HTML content.

## Customization

- Edit `template.html` to change the global layout, navigation menu, or include custom CSS and JavaScript.
- Add or remove Markdown features by extending the conversion functions in `src/utils/`.
- Place additional static assets (fonts, icons) in `static/`—they will be copied automatically.

## Running Tests

To verify that Markdown parsing and HTML conversion behave correctly:

```bash
./test.sh
```

Tests cover parsing headings, lists, code blocks, inline formatting, and ensuring directory structure mirroring.

## Deployment to GitHub Pages

1. Push your repository with the generated `docs/` folder. Configure GitHub Pages to serve from the `docs/` directory on the `main` branch.
2. Alternatively, use the provided GitHub Actions workflow to automate the build and deploy process.

## License

This project is released under the MIT License. Feel free to use and modify it for personal or commercial projects.

## Contributing & Future Enhancements

I welcome collaboration, feature requests, and bug reports! Some ideas for potential enhancements:

- **Custom CSS Themes**: Allow users to switch between multiple built‐in CSS themes or provide their own via a configuration file.
- **Markdown Extensions**: Add support for tables, footnotes, task lists, and other CommonMark extensions.
- **Nested Inline Formatting**: Support for italic text inside bold or other complex inline nesting.

Feel free to open issues or submit pull requests on GitHub—let’s make this generator even more powerful together!

# Static Site Generator (SSG)

This repository contains a simple Python based static site generator that converts Markdown files into a fully static HTML website.

## Features

- **Markdown to HTML** – Parses Markdown content into HTML using a lightweight conversion pipeline.
- **Template Rendering** – Injects converted HTML into a template so all pages share the same layout and styling.
- **Recursive Generation** – Walks the `content/` directory and builds a matching tree of HTML files in `docs/`.
- **Static Assets** – Copies the `static/` folder (CSS, images, etc.) directly into the output directory.

## Getting Started

1. **Install Python 3** – The scripts expect Python 3 to be available in your environment.
2. **Build the site**
   ```bash
   ./build.sh
   ```
   Generated files will appear in the `docs/` directory.
3. **Serve locally** (optional)
   ```bash
   ./main.sh
   ```
   This runs a simple development server on port `8888` so you can preview the output in a browser.

## Project Structure

- `content/` – Markdown source files.
- `static/` – Static assets (CSS, images, etc.) copied to `docs/` during the build.
- `template.html` – Base HTML template used for every generated page.
- `src/` – Python source code for the generator.
- `docs/` – Generated site output. This directory is created/overwritten during each build.
- `tests/` – Unit tests covering the converter and parser logic.

## Running Tests

Execute all unit tests with:

```bash
./test.sh
```

## Why This Project?

This SSG demonstrates practical understanding of Python scripting, file I/O, and basic HTML generation. It showcases the ability to take raw Markdown files and programmatically produce a static website—useful skills for automating documentation or blog creation.

Feel free to explore the code and modify the templates or Markdown content to generate your own site!

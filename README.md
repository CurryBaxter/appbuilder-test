# Nuxt 3 + @pharen/ui Example

This project demonstrates a minimal Nuxt 3 frontend using the `@pharen/ui` component library.

## Setup

1.  Install dependencies:

    ```bash
    cd frontend
    npm install
    ```

2.  Run the development server:

    ```bash
    npm run dev
    ```

3.  Open your browser and navigate to `http://localhost:3000/calculator`.


## Project Structure

-   `frontend/`: Contains the Nuxt 3 frontend application.
    -   `components/`: Reusable Vue components.
        -   `Calculator.vue`: A simple calculator component.
    -   `pages/`: Nuxt pages.
        -   `calculator.vue`: The calculator page.
    -   `plugins/`: Nuxt plugins.
        -   `pharen-ui.ts`: Registers the `@pharen/ui` library.
    -   `nuxt.config.ts`: Nuxt configuration file.
    -   `package.json`: Project dependencies and scripts.
-   `README.md`: This file.

# Nuxt 3 Frontend with @pharen/ui

This is a minimal Nuxt 3 frontend project using the `@pharen/ui` component library.

## Project Structure

- `frontend/`: Contains the Nuxt 3 frontend application.
  - `package.json`: Lists dependencies and scripts.
  - `nuxt.config.ts`: Nuxt configuration file.
  - `plugins/pharen-ui.ts`: Registers the `@pharen/ui` plugin.
  - `components/Calculator.vue`: A simple calculator component with two inputs and four operators.
  - `pages/calculator.vue`: A page that renders the calculator component.
- `README.md`: This file.

## Usage

1.  **Install dependencies:**

    ```bash
    cd frontend
    npm install
    ```

2.  **Run the development server:**

    ```bash
    npm run dev
    ```

    This will start the Nuxt development server, and you can access the application at `http://localhost:3000` (or the port specified by Nuxt).

3.  **Access the calculator:**
    Navigate to `/calculator`.

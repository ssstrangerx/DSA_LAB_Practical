import webbrowser

def run_browser_simulation():
    history = []        
    forward = []        
    def visit(page: str):
        if not page:
            print("Page name cannot be empty.")
            return
        history.append(page)
        forward.clear()  
        print(f"Visited: {page}")
        url = page
        webbrowser.open(url)

    def go_back():
        if not history:
            print("No pages in history.")
            return
        popped = history.pop()
        forward.append(popped)
        print(f"Going back from: {popped}")
        if history:
            print(f"Current page: {history[-1]}")
        else:
            print("No pages left in history.")

    def delete_history():
        history.clear()
        forward.clear()
        print("History cleared.")

    def go_forward():
        if not forward:
            print("No pages in forward stack.")
            return
        page = forward.pop()
        history.append(page)
        print(f"Going forward to: {page}")
        print(f"Current page: {history[-1]}")

    def show_history():
        if not history:
            print("History is empty.")
        else:
            print("History:", " -> ".join(history))

    def current_page():
        if not history:
            print("No current page.")
        else:
            print("Current page:", history[-1])

    menu = (
        "\nCommands:\n"
        " visit <page>   - Visit a new page\n"
        " back           - Go back\n"
        " forward        - Go forward\n"
        " current        - Show current page\n"
        " show           - Show full history\n"
        " exit           - Exit simulation\n"
        " delete         - Clear history\n"
    )

    print("Browser Back/Forward Simulation")
    print(menu)

    while True:
        cmd = input(">>> ").strip()
        if not cmd:
            continue

        parts = cmd.split(maxsplit=1)
        action = parts[0].lower()

        if action == "visit":
            page = parts[1].strip() if len(parts) > 1 else ""
            visit(page)
        elif action == "back":
            go_back()
        elif action == "forward":
            go_forward()
        elif action == "current":
            current_page()
        elif action == "show":
            show_history()
        elif action == "delete":
            delete_history()
        elif action == "exit":
            print("Exiting browser simulation.")
            break
        else:
            print("Unknown command. Type 'visit <page>' or 'back' or 'forward' or 'show' or 'current' or 'exit'.")

if __name__ == "__main__":
    run_browser_simulation()

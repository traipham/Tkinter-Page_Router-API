import router

if __name__ == "__main__":
    # Create main window
    root = router.Router()
    root.center_window()
    root.title("Test Router Module")

    root.append_new_page("First Page")
    root.append_new_page("Second Page")
    # Display window
    root.mainloop()     
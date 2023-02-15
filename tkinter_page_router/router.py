import tkinter as tk
from tkinter import TOP, ttk

class Router(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Initialize main frame for app
        self.master_frame = tk.Frame(self)
        self.master_frame.pack(side = "top", fill = "both", expand = True)
        # Make widgets scalable to window size
        self.master_frame.grid_rowconfigure(0, weight=1)
        self.master_frame.grid_columnconfigure(0, weight=1)

        # button frame
        self.button_frame = tk.Frame(self.master_frame)
        self.game_frame = tk.Frame(self.master_frame)
        self.tool_frame = tk.Frame(self.master_frame)
        self.button_frame.grid(row=0, column=0, sticky="nsew")
        # self.game_frame.grid(row=0, column=1,  sticky="nsew")
        # self.tool_frame.grid(row=0, column=2,  sticky="nsew")

        # Collect all pages 
        self.pages = {}
        self.pages["button_frame"] = self.button_frame
        if len(self.pages) > 0:
            for name, page in self.pages.items():
                print(f"Displaying: {name}")
                page.grid(row=0, column=0, sticky="nsew")

        self.button_frame.tkraise()         # show the button_Frame page first

    
    def display_page(self, page_name: str):
        """Display frame when next page clicked"""
        self.pages[page_name].grid(row=0, column=0, sticky="nsew")
        frame = self.pages[page_name]
        frame.tkraise()                     # display page on click of button
        print(f"Displaying: {page_name}")
    
    def return_to_menu(self):
        """Return to main page"""
        print(f"Displaying: Main page")
        self.button_frame.tkraise()

    def append_new_page(self, page_name: str):
        """Add new buttons that links to new page/frame"""
        self.pages[page_name]= Page(self, self.master_frame, page_name)  

        self.add_buttons(page_name)
        self.button_frame.tkraise()         # create new page, but still display button frame

    def add_buttons(self, page_name):
        """Add and display buttons on master frame, this should be in Menu_page"""
        button = tk.Button(self.button_frame, text=f"Go to {page_name}", command=lambda: self.display_page(page_name))

        # button.grid(row=len(self.pages), column=0)
        button.pack(side="top", pady=20)
    
    def center_window(self, width: int = 1080, height: int = 720):
        self.window_width = width
        self.window_height = height
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        center_width = int(self.screen_width/2 - self.window_width/2)
        center_height = int(self.screen_height/2 - self.window_height/2)
        self.geometry(f"{self.window_width}x{self.window_height}+{center_width}+{center_height}")

class Page(tk.Frame):
    def __init__(self, root_tk, parent, page_name):
        tk.Frame.__init__(self, parent)
        self.name = page_name
        self.button_frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.game_frame = tk.Frame(self, highlightbackground="blue", highlightthickness=2)
        self.title_label = tk.Label(self.game_frame, text=f"{self.name} Page")
        self.return_button = tk.Button(self.button_frame, text="Return to Menu", command=lambda: root_tk.return_to_menu())

        self.columnconfigure(1, weight=1)

        self.button_frame.grid(row=0, column=0)
        tk.Frame(self).grid(row=0, column=2)
        self.game_frame.grid(row=1, column=1)
        self.title_label.grid(row=0, column=0)
        self.return_button.pack(side=TOP, anchor="n", padx=20, pady=10)

    def set_title(self, title: str):
        self.title_label.config(text=f"{title}")
    

# if __name__ == "__main__":
#     # Create main window
#     root = Router()
#     root.center_window()
#     root.title("Test Router Module")

#     root.append_new_page("First Page")
#     root.append_new_page("Second Page")
#     # Display window
#     root.mainloop()

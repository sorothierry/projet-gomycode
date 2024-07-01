

import tkinter as tk
from tkinter import messagebox, filedialog

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Projet d'Application Etudiant")

        self.projects = []
        
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        
        # Login Screen
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=50)

        self.username_label = tk.Label(self.login_frame, text="Nom d'utilisateur:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.password_label = tk.Label(self.login_frame, text="Mot de Passe:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.login_button = tk.Button(self.login_frame, text="Connexion", command=self.login)
        self.login_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Simple username/password validation (for demonstration purposes)
        if username == "soro" and password == "01999":
            self.create_main_screen()
        else:
            messagebox.showerror("Connexion échoué", "Nom d'Utilisateur ou Mot de Passe invalide")
    
    def create_main_screen(self):
        self.clear_screen()

        # Main Screen
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        self.idea_label = tk.Label(self.main_frame, text="Titre du Projet:")
        self.idea_label.grid(row=0, column=0, padx=10, pady=5)
        self.idea_entry = tk.Entry(self.main_frame, width=50)
        self.idea_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.use_cases_label = tk.Label(self.main_frame, text="Explication du Projet:")
        self.use_cases_label.grid(row=1, column=0, padx=10, pady=5)
        self.use_cases_text = tk.Text(self.main_frame, height=10, width=50)
        self.use_cases_text.grid(row=1, column=1, padx=10, pady=5)
        
        self.actors_label = tk.Label(self.main_frame, text="Acteur Potentiel:")
        self.actors_label.grid(row=2, column=0, padx=10, pady=5)
        self.actors_text = tk.Text(self.main_frame, height=10, width=50)
        self.actors_text.grid(row=2, column=1, padx=10, pady=5)
        
        self.submit_button = tk.Button(self.main_frame, text="Soumettre", command=self.submit)
        self.submit_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        self.view_projects_button = tk.Button(self.main_frame, text="Voir Projet", command=self.view_projects)
        self.view_projects_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        self.export_projects_button = tk.Button(self.main_frame, text="Exporter le  Projet", command=self.export_projects)
        self.export_projects_button.grid(row=5, column=1, padx=10, pady=10, sticky="e")
        
    def submit(self):
        idea = self.idea_entry.get()
        use_cases = self.use_cases_text.get("1.0", tk.END).strip()
        actors = self.actors_text.get("1.0", tk.END).strip()
        
        if not idea or not use_cases or not actors:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
        else:
            project = {
                "idea": idea,
                "use_cases": use_cases,
                "actors": actors
            }
            self.projects.append(project)
            messagebox.showinfo("Projet soumis", "Votre projet à bien été soumis avec succes.")
            self.clear_form()

    def clear_form(self):
        self.idea_entry.delete(0, tk.END)
        self.use_cases_text.delete("1.0", tk.END)
        self.actors_text.delete("1.0", tk.END)
        
    def view_projects(self):
        self.clear_screen()

        self.projects_frame = tk.Frame(self.root)
        self.projects_frame.pack(pady=20)

        self.projects_listbox = tk.Listbox(self.projects_frame, width=100, height=20)
        self.projects_listbox.pack(padx=10, pady=10)

        for i, project in enumerate(self.projects):
            self.projects_listbox.insert(tk.END, f"Project {i+1}: {project['idea']}")

        self.back_button = tk.Button(self.projects_frame, text="Back", command=self.create_main_screen)
        self.back_button.pack(pady=10)

    def export_projects(self):
        if not self.projects:
            messagebox.showwarning("Export Error", "No projects to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                for i, project in enumerate(self.projects):
                    file.write(f"Project {i+1}:\n")
                    file.write(f"Idea: {project['idea']}\n")
                    file.write(f"Use Cases:\n{project['use_cases']}\n")
                    file.write(f"Potential Actors:\n{project['actors']}\n")
                    file.write("\n---\n\n")
            messagebox.showinfo("Export Successful", "Projects exported successfully.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

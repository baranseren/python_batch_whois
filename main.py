import tkinter as tk
from tkinter import scrolledtext
import whois

def check_domains():
    domains_input = domain_text.get("1.0", tk.END).strip()
    domain_list = domains_input.splitlines()

    result_text.delete("1.0", tk.END)
    
    for domain in domain_list:
        domain = domain.strip()
        if not domain:
            continue

        try:
            w = whois.whois(domain)
            if w.domain_name:
                result_text.insert(tk.END, f"{domain} -> ALINMIŞ\n")
            else:
                result_text.insert(tk.END, f"{domain} -> BOŞTA\n")
        except:
            result_text.insert(tk.END, f"{domain} -> BOŞTA (veya kontrol edilemedi)\n")

root = tk.Tk()
root.title("Domain Satın Alınabilirlik Kontrolü")

# Form penceresini büyütmek için
root.geometry("800x600")

label = tk.Label(root, text="Kontrol etmek istediğiniz domainleri her satıra bir tane gelecek şekilde girin:")
label.pack(pady=5)

domain_text = scrolledtext.ScrolledText(root, width=80, height=15)
domain_text.pack(padx=10, pady=5)

check_button = tk.Button(root, text="Kontrol Et", command=check_domains)
check_button.pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=80, height=15)
result_text.pack(padx=10, pady=5)

root.mainloop()

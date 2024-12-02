from motor.find_color_name import find_color_name
import replicate

def generate_moodboard(prompt):
    """Gera um moodboard com base na prompt fornecida."""
    # Chama o modelo Replicate para gerar o moodboard
    output = replicate.run(
        "black-forest-labs/flux-schnell",
        input={"prompt": prompt, "num_outputs": 4},
    )
    
    return output

def generate_moodboard_with_harmonies(prompt, color_harmonies):
    """Gera um moodboard com base na prompt fornecida."""
    # Chama o modelo Replicate para gerar o moodboard
    # Transforma o dicion rio de harmonias em um texto
    harmonies_text = []
    for name, colors in color_harmonies.items():
        name = name.replace("_", " ")
        harmonies_text.append(f"{name}: {', '.join(find_color_name(color) for color in colors)}")
    harmonies_text = "\n".join(harmonies_text)
    
    final_prompt = f"""{prompt}. \n Use one of the following color harmonies and colors associated: {harmonies_text}"""
    
    output = replicate.run(
        "black-forest-labs/flux-schnell",
        input={"prompt": final_prompt, "num_outputs": 4},
    )
    
    print(final_prompt)
    
    return output
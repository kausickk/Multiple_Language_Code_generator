import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

def generate_code(prompt):
    completion = client.chat.completions.create(
        model="meta/llama3-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=False
    )
    try:
        response_text = completion.choices[0].text.strip()  # Access the 'text' attribute directly
    except AttributeError:
        response_text = completion.choices[0].message  # Fallback if 'text' is not available
    
    return response_text

def extract_code(response_text, language):
    start = response_text.find(f"**{language}**")
    if start == -1:
        return ""
    end = response_text.find("**", start + len(f"**{language}**") + 1)
    if end == -1:
        return ""
    return response_text[start:end].strip()

st.title("Code Generator")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        response_text = generate_code(prompt)
        
        response = {
            "JavaScript": extract_code(response_text, "JavaScript"),
            "Python": extract_code(response_text, "Python"),
            "Java": extract_code(response_text, "Java"),
            "C++": extract_code(response_text, "C++"),
            "C#": extract_code(response_text, "C#")
        }
        
        st.subheader("Generated Code Snippets")
        
        if response["JavaScript"]:
            st.markdown("### JavaScript")
            st.code(response["JavaScript"])
        
        if response["Python"]:
            st.markdown("### Python")
            st.code(response["Python"])
        
        if response["Java"]:
            st.markdown("### Java")
            st.code(response["Java"])
        
        if response["C++"]:
            st.markdown("### C++")
            st.code(response["C++"])
        
        if response["C#"]:
            st.markdown("### C#")
            st.code(response["C#"])
    else:
        st.error("Please enter a prompt.")

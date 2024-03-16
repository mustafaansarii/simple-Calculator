import gradio as gr

def smart_calculator(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

iface = gr.Interface(fn=smart_calculator, 
                      inputs=gr.Textbox(lines=2, label="Enter expression"),
                      outputs="text",
                      title="Simple Calculator")

iface.launch()

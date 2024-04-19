from pathlib import Path

cwd = Path(__file__).parent / "jx3apifun"
interface = cwd / "interface.py"
async_interface = cwd / "interface_async.py"

with (
    open(interface, "r", encoding="utf-8") as f,
    open(async_interface, "w", encoding="utf-8") as g,
):
    text = f.read()
    text = text.replace("ApiInterface", "ApiInterfaceAsync")
    text = text.replace("def ", "async def ")
    g.write(text)

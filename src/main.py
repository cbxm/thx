# import dearpygui.dearpygui as dpg
import gui


# def fakegui():
#     dpg.create_context()
#     dpg.create_viewport(title="custom title", width=600, height=300)

#     with dpg.window(label="Example Window"):
#         dpg.add_text("gm, world")
#         dpg.add_button(label="gm")

#     dpg.setup_dearpygui()
#     dpg.show_viewport()
#     dpg.start_dearpygui()
#     dpg.destroy_context()


def main():
    gui.launch()


if __name__ == "__main__":
    main()

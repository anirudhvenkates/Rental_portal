from UI.ui_handler import UserInterfaceHandler

if __name__ == '__main__':
    # Instantiate the handler and get the appropriate UI based on some condition
    ui_handler = UserInterfaceHandler(ui_type='simple')  # Set 'simple' or 'complex' as per requirement

    # Get the UI function based on the ui_type and call it
    ui_function = ui_handler.get_ui()
    ui_function()

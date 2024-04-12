import sys

arg1 = sys.argv.pop()

if arg1 == "ui:admin":
    from app.ui.admin.main import start
    start()

elif arg1 == "cli:admin":
    from app.lib.cli.admin import main
    main()

elif arg1 == "cli:client":
    from app.lib.cli.client import main
    main()

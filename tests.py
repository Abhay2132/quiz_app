import sys

arg1 = sys.argv.pop()

if arg1 == "ui:admin":
    from app.ui.admin.main import start
    start()

elif arg1 == "cli:admin":
    from app.cli.admin import main
    main()

elif arg1 == "cli:client":
    from app.cli.client import main
    main()

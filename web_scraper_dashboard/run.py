from web_scraper_dashboard.app.auth import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
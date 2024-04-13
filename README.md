# Wordpress-Scanner

Python script that performs scanning and enumeration on WordPress websites. The script checks for various vulnerabilities and information disclosures, such as backup wp-config.php files, exposed log files, user enumeration, potential denial of service issues, and more. The script seems to be well-structured and uses the requests, json, re, time, BeautifulSoup, and colorama libraries for web scraping, handling HTTP requests, and adding colors to the output.

# Working 

  - It starts by taking a website URL as input, then it checks if the website is up and running.
  - If WordPress is detected on the website, it fetches details like the website name, description, and installed plugins.
  - It then proceeds to scan for vulnerabilities and potential information disclosures, such as backup wp-config.php files, exposed log files, user enumeration, and possible denial of service issues.
  - Finally, it writes the results to a text file with a timestamp.


# WordPress Scanner Vulnerability Checks

  - Outdated WordPress Version
  - Vulnerable Plugins
  - Weak Passwords
  - File Permission Issues
  - Cross-Site Scripting (XSS)
  - SQL Injection
  - Cross-Site Request Forgery (CSRF)
  - Security Misconfigurations

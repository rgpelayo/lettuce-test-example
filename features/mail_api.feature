Feature: Fill out the API method for mail on the API Workshop page and send an email
	Scenario: Fill out the Mail API method and verify mail is sent
		Given I am on the SendGrid login page
			Log on
		Given I am on the API Workshop page
			Enter my credentials
			Expand the Mail method
			When I fill the to field with "rgpelayo@aol.com"
			When I fill the toname field with "rowena pelayo"
			When I fill the x-smtpapi field with "{"to": "[rowena pelayo <rgpelayo@aol.com>]"}"
			When I fill the from field with "rgpelayo@gmail.com"
			When I fill the fromname field with "rowena g pelayo"
			When I fill the subject field with "lettuce test it"
			When I fill the text field with "sending via lettuce"
			When I fill the html field with "<html><body>sending via lettuce</body></html>"
			When I fill the bcc field with "rowena.pelayo@aol.com"
			When I fill the date field with "Sun, 03 Nov 2013 02:06:11 -0000"
			When I fill the headers field with "{"X-Accept-Language": "en", "X-Mailer": "MyApp"}"
			When I fill the files field with "files[file1.doc]=example.doc&files[file2.pdf]=example.pdf"
			When I click the Try It button
			Then the response body should return "success"

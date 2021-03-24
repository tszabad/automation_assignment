function myFunction() {
    var persons = Sheets.Spreadsheets.Values.get("17eUsQ0F2ZZX7wjyxg_xnpPEnYgu1KbunOC19oyve_Xc","A2:A6");
    Logger.log(persons.values)
    MailApp.sendEmail({
      to:"tszabad@gmail.com",
      subject: "",
      htmlBody: "The very first person is: " + persons.values[1][0]
    });
    var form = FormApp.create('Famous persons Form');
    var item = form.addCheckboxItem();
    item.setTitle('Which is your favorite famous person?');
    item.setChoices([
          item.createChoice(persons.values[1][0]),
          item.createChoice(persons.values[2][0]),
          item.createChoice(persons.values[3][0]),
          item.createChoice(persons.values[4][0])
      ]);
    Logger.log('Published URL: ' + form.getPublishedUrl());
    Logger.log('Editor URL: ' + form.getEditUrl());
    
  }
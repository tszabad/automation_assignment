function myFunction() {
  var persons = Sheets.Spreadsheets.Values.get("1mtRtZDah5zB-ifd984OFvgn39aCcuWEwHr53g-ydaqw","A2:A6");
  Logger.log(persons.values)
  var form = FormApp.create('Movies cast member voting form');
  var item = form.addCheckboxItem();
  item.setTitle('Which is your favorite cast memeber?');
  item.setChoices([
        item.createChoice(persons.values[0][0]),
        item.createChoice(persons.values[1][0]),
        item.createChoice(persons.values[2][0]),
        item.createChoice(persons.values[3][0]),
        item.createChoice(persons.values[4][0])
        

    ]);
  Logger.log('Published URL: ' + form.getPublishedUrl());
  Logger.log('Editor URL: ' + form.getEditUrl());

  MailApp.sendEmail({
    to:"tszabad@gmail.com",
    subject: "cast memebers voting",
    htmlBody: "Dear Friend! \n Please answer this form: \n" + form.getPublishedUrl() +"\nThank you for answering! \n Best wishes! \n Tamás"
  });
  
}
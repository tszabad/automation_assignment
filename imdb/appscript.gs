function myFunction() {
  const PERSONS = Sheets.Spreadsheets.Values.get("1mtRtZDah5zB-ifd984OFvgn39aCcuWEwHr53g-ydaqw","A2:A6");
  const EMAILS = Sheets.Spreadsheets.Values.get("1wmFx8Wmi2vZJVPDijsg7ADldpfyV9o9U33n8uQKGjqs", "A1:A");
  Logger.log(PERSONS.values)
  let form = FormApp.create('Movies cast member voting form');
  let item = form.addCheckboxItem();
  item.setTitle('Which is your favorite cast memeber?');
  item.setChoices([
        item.createChoice(PERSONS.values[0][0]),
        item.createChoice(PERSONS.values[1][0]),
        item.createChoice(PERSONS.values[2][0]),
        item.createChoice(PERSONS.values[3][0]),
        item.createChoice(PERSONS.values[4][0])
        
    ]);
  Logger.log('Published URL: ' + form.getPublishedUrl());
  Logger.log('Editor URL: ' + form.getEditUrl());

  let subject = "cast memebers voting"
  let body = "Dear Friend! \n Please answer this form: "+"\n" + form.getPublishedUrl() +"\n"+"Thank you for answering! "+"\n"+" Best wishes! "+"\n "+"Tamás" 
  for (let value of EMAILS.values) {
    let receiver = String(value[0])
    MailApp.sendEmail(recipient=receiver, subject=subject, body=body)
    Logger.log('Email sent to ' + receiver);
  }
}

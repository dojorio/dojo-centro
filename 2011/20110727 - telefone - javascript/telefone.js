function getPhoneNumber(expression) {
    var phone_keys = {
        'ABC': '2',
        'DEF': '3',
        'GHI': '4',
        'JKL': '5',
        'MNO': '6',
        'PQRS': '7',
        'TUV': '8',
        'WXYZ': '9'
    };
    
    var regexp, pattern, phone_number = expression;
    
    for (var phone_key in phone_keys) {
        pattern = '[' + phone_key + ']';
        
        regexp = new RegExp(pattern, 'g');
        numero = phone_keys[phone_key]
        
        phone_number = phone_number.replace(regexp, numero);
    }
        
    return phone_number;
}
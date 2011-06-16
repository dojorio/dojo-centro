def separar_url(url)
    tokens = {}

    if url.include?('://')
        tokens['protocolo'], url = url.split('://', 2)
    end
    
    host, url = url.split('/', 2)
    
    if host.include?(':')
        host, tokens['porta'] = host.split(':', 2)
    end
    
    tokens['host'] = host
    if not url.nil?
        if url.include?('?')
            url, parametro = url.split('?', 2)
            chave, valor = parametro.split('=', 2)
            tokens['parametro'] = {chave => valor} 
        end
        tokens['path'] = '/' + url
    end
 
    return tokens
    
end

describe 'separar_url' do 
    it "deve aceitar um dominio" do
        tokens = separar_url('google.com')
        tokens.should == { 'host' => 'google.com' }
    end
    
    it "deve aceitar um dominio diferente" do
        tokens = separar_url('gmail.com')
        tokens.should == { 'host' => 'gmail.com' }
    end

    it "verifica o protocolo usado" do
        tokens = separar_url('http://google.com')
        tokens.should == {
            'protocolo' => 'http',
            'host' => 'google.com'
        }
    end
    
    it "verifica o path usado" do
        tokens = separar_url('google.com/mail/')
        tokens.should == {
            'host' => 'google.com',
            'path' => '/mail/'
        }
    end

    it "deve aceitar protocolo, host e path" do
        tokens = separar_url('http://google.com/mail/')
        tokens.should == {
            'protocolo' => 'http',
            'host' => 'google.com',
            'path' => '/mail/'
        }
    end
    it "deve aceitar host e porta" do
        tokens = separar_url('google.com:80')
        tokens.should == {
        'host' => 'google.com',
        'porta' => '80'
        }
    end

    it "deve aceitar host, porta e path" do
        tokens = separar_url('google.com:80/mail/')
        tokens.should == {
        'host' => 'google.com',
        'porta' => '80',
        'path' => '/mail/'
        }
    end

    it "deve aceitar protocolo, host, porta e path" do
        tokens = separar_url('http://google.com:80/mail/')
        tokens.should == {
        'protocolo' => 'http',
        'host' => 'google.com',
        'porta' => '80',
        'path' => '/mail/'
        }
    end
    
    it "deve aceitar protocolo, host, porta e path e parametro" do
        tokens = separar_url('http://google.com:80/mail/?user=fulano')
        tokens.should == {
        'protocolo' => 'http',
        'host' => 'google.com',
        'porta' => '80',
        'path' => '/mail/',
        'parametro' => {'user' => 'fulano'},
        }
    end
 end

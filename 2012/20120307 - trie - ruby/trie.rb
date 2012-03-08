class Trie
  def initialize
    @root = {}
  end

  def add(id, term)
    current = @root
    term.split('').each do |char|
      current[char] = {} if current[char].nil?
      current = current[char]
    end
    current[:indices] = [] if current[:indices].nil?
    current[:indices] << id
  end
  
  def find(word)
    current = @root
    word.split('').each do |char|
      return [] if current[char].nil?
      current = current[char]
    end
    return (current[:indices] or [])
  end
  
  def dictionary
    @root
  end
end


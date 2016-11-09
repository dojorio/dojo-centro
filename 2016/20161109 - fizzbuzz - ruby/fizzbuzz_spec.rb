require_relative 'fizzbuzz'

describe("fizzbuzz") do
  it("is 1 to 1") do
    expect(fizzbuzz(1)).to(eq(1))
  end
end

def ballroom(height, width, planks)
  area = width * height
  planks.sort!.reverse!

  while planks.size > 0
    sum = 0
    count = 0

    planks.each do |plank|
      return 1 if plank == area

      if sum + plank <= area
        sum += plank
        count += 1

        return count if sum == area
      end
    end

    planks.shift
  end

  "impossivel"
end
def ballroom(height, width, planks)
  area = width * height
  perms = planks.permutation

  for perm in perms
    sum = 0
    count = 0

    perm.each do |plank|
      return 1 if plank == area

      if sum + plank <= area
        sum += plank
        count += 1

        return count if sum == area
      end
    end
  end

  "impossivel"
end
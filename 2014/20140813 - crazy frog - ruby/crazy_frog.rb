def bigger_jump(distance, stones)
  if distance-1 == 2
    return 2
  end
  if !stones.empty?
    return 1;
  end
  return distance;
end
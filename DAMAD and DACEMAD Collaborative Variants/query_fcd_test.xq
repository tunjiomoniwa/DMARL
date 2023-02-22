
  for $kk in doc("fcd_dcc.xml") //timestep
    where $kk/@time> 0.00 and $kk/@time< 1500.00
    return
    <step time = '{$kk/@time}'>
     {
      $kk}    
    
    </step>


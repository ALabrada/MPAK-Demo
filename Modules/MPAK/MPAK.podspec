Pod::Spec.new do |s|

s.name                  = 'MPAK'
s.version               = '2022.06.20'
s.license               = 'IVCS'
s.summary               = 'IVCS'
s.homepage              = 'IVCS'
s.author                = 'IVCS'
s.source                = { :git => 'https://fake.com/FAKE.git', :tag => s.version }
s.source_files          = 'src/*.swift'
s.swift_version         = '5.2'
s.ios.deployment_target = '14.0'

end

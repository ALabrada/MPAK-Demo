Pod::Spec.new do |s|

s.name                  = 'Home'
s.version               = '2023.12.03'
s.license               = 'IVCS'
s.summary               = 'IVCS'
s.homepage              = 'IVCS'
s.author                = 'IVCS'
s.source                = { :git => 'https://fake.com/FAKE.git', :tag => s.version }
s.source_files          = '**/**/*.{swift,yml}'
s.swift_version         = '5.2'
s.ios.deployment_target = '14.0'
s.dependency 'MPAK'
s.dependency 'Net'
end

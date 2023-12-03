# Uncomment the next line to define a global platform for your project
platform :ios, '14.0'

target 'demo' do
  # Comment the next line if you don't want to use dynamic frameworks
  use_frameworks!

  # Pods for demo
  pod 'Parse' 
  
  # Modules
  pod 'Home', :path => 'Modules/Home'
  pod 'HomeSlot', :path => 'Modules/HomeSlot'
  pod 'Login', :path => 'Modules/Login'
  pod 'LoginSlot', :path => 'Modules/LoginSlot'
  pod 'MPAK', :path => 'Modules/MPAK'
  pod 'Net', :path => 'Modules/Net'

end

post_install do |installer|
  installer.generated_projects.each do |project|
    project.targets.each do |target|
      target.build_configurations.each do |config|
        config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '14.0'
        config.build_settings['CODE_SIGNING_ALLOWED'] = 'NO'
      end
    end
  end
end

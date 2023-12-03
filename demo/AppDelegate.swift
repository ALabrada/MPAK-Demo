//
//  AppDelegate.swift
//  demo
//
//  Created by Administrator on 03.12.2023.
//

import HomeSlot
import LoginSlot
import Net
import Parse
import SwiftUI

class AppDelegate: NSObject, UIApplicationDelegate {

  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {

    let configuration = ParseClientConfiguration {
      $0.applicationId = "DHixOY0WKShJLvgmEQ8eHEggIFaGAdP8dqToDBtI"
      $0.clientKey = "eSbQP8Jfh6GOkHCLEYtAguNAgI0rWnc4fv2yJxgp"
      $0.server = "https://parseapi.back4app.com"
    }
    Parse.initialize(with: configuration)

    LoginSlot.setup(
      { Net.Publisher() }
    )

    HomeSlot.setup(
      { Net.Publisher() }
    )

    return true
  }

}

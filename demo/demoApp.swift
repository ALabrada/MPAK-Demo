//
//  demoApp.swift
//  demo
//
//  Created by Administrator on 03.12.2023.
//

import SwiftUI

@main
struct demoApp: App {
  @UIApplicationDelegateAdaptor(AppDelegate.self) private var appDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

import SwiftUI

extension LoginCanvas {
  public struct V: View {
    @ObservedObject private var vm: VM

    init(_ vm: VM) {
      self.vm = vm
    }

    public var body: some View {
      Text("Hello World!")
    }
  }
}

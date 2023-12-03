import Login
import Net

public enum LoginSlot {
  static var services: [AnyObject] = []

  public static func setup(
    _ net: @escaping () -> Net.Publisher
  ) {
    let loginCW = LoginCanvas.World()

    services = [
      LoginCanvas.Service(loginCW)
    ]
  }
}

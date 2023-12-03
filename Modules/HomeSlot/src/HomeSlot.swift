import Home
import Net

public enum HomeSlot {
  static var services: [AnyObject] = []

  public static func setup(
    _ net: @escaping () -> Net.Publisher
  ) {
    let loginCW = HomeCanvas.World()

    services = [
      HomeCanvas.Service(loginCW)
    ]
  }
}

// ВНИМАНИЕ Сгенерировано автоматом из файла LoginCanvas.yml
// ВНИМАНИЕ Не менять руками!

import Combine
import MPAK
import os

// MARK: - Context

public protocol LoginCanvasContext {

}

// MARK: - Controller

extension LoginCanvas {
  final class Controller: MPAK.Controller<LoginCanvas.Model> {
    private let log = Logger(subsystem: Bundle.main.bundleIdentifier!, category: "LoginCanvas")

    init() {
      super.init(
        LoginCanvas.Model(),
        debugClassName: "LoginCCtrl",
        debugLog: { [log] ln in log.debug("\(ln, privacy: .public)") }
      )
    }
  }



  // MARK: - Model

  public struct Model: LoginCanvasContext {

  }

  // MARK: - Service

  public final class Service {
    let ctrl = Controller()
    let world: World

    var subscriptions = [AnyCancellable]()
    static private(set) weak var singleton: Service?

    public init(_ world: World) {
      self.world = world
      Self.singleton = self

    }
  }

  // MARK: - World

  public struct World {


    public init(

    ) {

    }
  }

  enum SectionGenerated {





  }
}

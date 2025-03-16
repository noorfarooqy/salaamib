<template>
  <div class="col-xl-6">
    <div class="card">
      <div class="card-body card-buttons">
        <h4 class="header-title">Modal with Pages</h4>
        <p>Examples of custom modals.</p>

        <!-- Signup modal content -->
        <div
          id="signup-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-body">
                <div class="text-center mt-2 mb-4">
                  <div class="auth-logo">
                    <router-link to="/dashboard/" class="logo logo-dark">
                      <span class="logo-lg">
                        <img src="@/assets/img/logo.png" alt="" height="42" />
                      </span>
                    </router-link>
                  </div>
                </div>

                <form class="px-3" action="javascript:;">
                  <div class="mb-3">
                    <label for="username" class="form-label">Name</label>
                    <input
                      class="form-control"
                      type="email"
                      id="username"
                      placeholder="Michael Zenaty"
                    />
                  </div>

                  <div class="mb-3">
                    <label for="emailaddress" class="form-label">Email address</label>
                    <input
                      class="form-control"
                      type="email"
                      id="emailaddress"
                      placeholder="john@deo.com"
                    />
                  </div>

                  <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input
                      class="form-control"
                      type="password"
                      id="password"
                      placeholder="Enter your password"
                    />
                  </div>

                  <div class="mb-3">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input" id="customCheck1" />
                      <label class="form-check-label" for="customCheck1"
                        >I accept <a href="javascript:;">Terms and Conditions</a></label
                      >
                    </div>
                  </div>

                  <div class="mb-3 text-center">
                    <b-button variant="primary" type="submit"> Sign Up Free </b-button>
                  </div>
                </form>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <!-- SignIn modal content -->
        <div
          id="login-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-body">
                <div class="text-center mt-2 mb-4">
                  <div class="auth-logo">
                    <router-link to="/dashboard/" class="logo logo-dark">
                      <span class="logo-lg">
                        <img src="@/assets/img/logo.png" alt="" height="42" />
                      </span>
                    </router-link>
                  </div>
                </div>

                <form action="javascript:;" class="px-3">
                  <div class="mb-3">
                    <label for="emailaddress1" class="form-label">Email address</label>
                    <input
                      class="form-control"
                      type="email"
                      id="emailaddress1"
                      placeholder="john@deo.com"
                    />
                  </div>

                  <div class="mb-3">
                    <label for="password1" class="form-label">Password</label>
                    <input
                      class="form-control"
                      type="password"
                      id="password1"
                      placeholder="Enter your password"
                    />
                  </div>

                  <div class="mb-3">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input" id="customCheck2" />
                      <label class="form-check-label" for="customCheck2"
                        >Remember me</label
                      >
                    </div>
                  </div>

                  <div class="mb-2 text-center">
                    <b-button pill variant="primary" type="submit"> Sign In </b-button>
                  </div>
                </form>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <div class="button-list">
          <!-- Sign Up modal -->
          <b-button
            variant="primary mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#signup-modal"
          >
            Sign Up Modal
          </b-button>
          <!-- Log In modal -->
          <b-button
            variant="info mt-1"
            data-bs-toggle="modal"
            data-bs-target="#login-modal"
          >
            Log In Modal
          </b-button>
        </div>
      </div>
      <!-- end card-body card-buttons -->
    </div>
    <!-- end card-->
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>

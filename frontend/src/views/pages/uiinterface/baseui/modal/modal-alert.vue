<template>
  <div class="col-xl-6">
    <div class="card">
      <div class="card-body card-buttons">
        <h4 class="header-title">Modal based Alerts</h4>
        <p>Show different contexual alert messages using modal component</p>

        <!-- Success Alert Modal -->
        <div
          id="success-alert-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-sm">
            <div class="modal-content modal-filled bg-success">
              <div class="modal-body p-4">
                <div class="text-center">
                  <i class="dripicons-checkmark h1 text-white"></i>
                  <h4 class="mt-2 text-white">Well Done!</h4>
                  <p class="mt-3 text-white">
                    Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                    dapibus ac facilisis in, egestas eget quam.
                  </p>
                  <b-button variant="light my-2" data-bs-dismiss="modal">
                    Continue
                  </b-button>
                </div>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <!-- Info Alert Modal -->
        <div
          id="info-alert-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-sm">
            <div class="modal-content">
              <div class="modal-body p-4">
                <div class="text-center">
                  <i class="dripicons-information h1 text-info"></i>
                  <h4 class="mt-2">Heads up!</h4>
                  <p class="mt-3">
                    Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                    dapibus ac facilisis in, egestas eget quam.
                  </p>
                  <b-button variant="info my-2" data-bs-dismiss="modal">
                    Continue
                  </b-button>
                </div>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <!-- Warning Alert Modal -->
        <div
          id="warning-alert-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-sm">
            <div class="modal-content">
              <div class="modal-body p-4">
                <div class="text-center">
                  <i class="dripicons-warning h1 text-warning"></i>
                  <h4 class="mt-2">Incorrect Information</h4>
                  <p class="mt-3">
                    Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                    dapibus ac facilisis in, egestas eget quam.
                  </p>
                  <b-button variant="warning my-2" data-bs-dismiss="modal">
                    Continue
                  </b-button>
                </div>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <!-- Danger Alert Modal -->
        <div
          id="danger-alert-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-sm">
            <div class="modal-content modal-filled bg-danger">
              <div class="modal-body p-4">
                <div class="text-center">
                  <i class="dripicons-wrong h1 text-white"></i>
                  <h4 class="mt-2 text-white">Oh snap!</h4>
                  <p class="mt-3 text-white">
                    Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                    dapibus ac facilisis in, egestas eget quam.
                  </p>
                  <b-button variant="light my-2" data-bs-dismiss="modal">
                    Continue
                  </b-button>
                </div>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <div class="button-list">
          <!-- Success Alert modal -->
          <b-button
            variant="success mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#success-alert-modal"
          >
            Success Alert
          </b-button>
          <!-- Info Alert modal -->
          <b-button
            variant="info mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#info-alert-modal"
          >
            Info Alert
          </b-button>
          <!-- Warning Alert modal -->
          <b-button
            variant="warning mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#warning-alert-modal"
          >
            Warning Alert
          </b-button>
          <!-- Danger Alert modal -->
          <b-button
            variant="danger mt-1"
            data-bs-toggle="modal"
            data-bs-target="#danger-alert-modal"
          >
            Danger Alert
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

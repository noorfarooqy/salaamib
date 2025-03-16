<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <ticketheader title="Tickets" text="New Tickets" />
      <searchfilter />
      <card />
      <tab />
      <!-- Ticket list -->
      <div class="comments">
        <!-- card -->
        <div class="card">
          <div class="card-body card-support">
            <div class="comments-details d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center describe-btn mt-0">
                <h6 class="fw-bolder text-gray-dark">Support for theme</h6>
                <span class="badge badge-pill bg-success-light ms-3">Resolved</span>
              </div>
              <a href="javascript:;" class="reply-comment d-flex text-gray-light"><span><i
                    class="feather feather-clock text-gray-light fw-normal me-2"></i></span><span
                  class="text-gray-light fw-normal">Just Now</span></a>
            </div>
            <div class="card-describe">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod
                tempor incididunt labore dolore magna aliqua. Ut enim minim veniam,
                nostrud exercitation ullamco laboris nisi ut aliquip ex commodo
                consequat. Duis aute non proident, sunt in culpa qui officia deserunt
                mollit anim id est laborum.
              </p>
            </div>
            <div class="describe-btn">
              <span class="badge bg-warning-light text-warning-light me-2">Medium</span>
              <span class="badge badge-gray-outline me-2">#4987</span>
              <span><i class="feather feather-message-square text-gray-light fw-normal me-2"></i>3</span>
            </div>
          </div>
        </div>
        <!-- /card -->

        <!-- card -->
        <div class="card">
          <div class="card-body card-support">
            <div class="comments-details d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center describe-btn mt-0">
                <h6 class="fw-bolder text-gray-dark">Verify your email</h6>
                <span class="badge badge-pill bg-success-light ms-3">Resolved</span>
              </div>
              <a href="javascript:;" class="reply-comment d-flex text-gray-light"><span><i
                    class="feather feather-clock text-gray-light fw-normal me-2"></i></span><span
                  class="text-gray-light fw-normal">Just Now</span></a>
            </div>
            <div class="card-describe">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod
                tempor incididunt labore dolore magna aliqua. Ut enim minim veniam,
                nostrud exercitation ullamco laboris nisi ut aliquip ex commodo
                consequat. Duis aute non proident, sunt in culpa qui officia deserunt
                mollit anim id est laborum.
              </p>
            </div>
            <div class="describe-btn">
              <span class="badge bg-danger-light text-danger-light me-2">High</span>
              <span class="badge badge-gray-outline me-2">#4987</span>
              <span><i class="feather feather-message-square text-gray-light fw-normal me-2"></i>3</span>
            </div>
          </div>
        </div>
        <!-- /card -->

        <!-- card -->
        <div class="card">
          <div class="card-body card-support">
            <div class="comments-details d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center describe-btn mt-0">
                <h6 class="fw-bolder text-gray-dark">Calling for help</h6>
                <span class="badge badge-pill bg-success-light ms-3">Resolved</span>
              </div>
              <a href="javascript:;" class="reply-comment d-flex text-gray-light"><span><i
                    class="feather feather-clock text-gray-light fw-normal me-2"></i></span><span
                  class="text-gray-light fw-normal">Just Now</span></a>
            </div>
            <div class="card-describe">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod
                tempor incididunt labore dolore magna aliqua. Ut enim minim veniam,
                nostrud exercitation ullamco laboris nisi ut aliquip ex commodo
                consequat. Duis aute non proident, sunt in culpa qui officia deserunt
                mollit anim id est laborum.
              </p>
            </div>
            <div class="describe-btn">
              <span class="badge bg-primary-light me-2">Low</span>
              <span class="badge badge-gray-outline me-2">#4987</span>
              <span><i class="feather feather-message-square text-gray-light fw-normal me-2"></i>3</span>
            </div>
          </div>
        </div>
        <!-- /card -->

        <!-- card -->
        <div class="card">
          <div class="card-body card-support">
            <div class="comments-details d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center describe-btn mt-0">
                <h6 class="fw-bolder text-gray-dark">Management</h6>
                <span class="badge badge-pill bg-success-light ms-3">Resolved</span>
              </div>
              <a href="javascript:;" class="reply-comment d-flex text-gray-light"><span><i
                    class="feather feather-clock text-gray-light fw-normal me-2"></i></span><span
                  class="text-gray-light fw-normal">Just Now</span></a>
            </div>
            <div class="card-describe">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod
                tempor incididunt labore dolore magna aliqua. Ut enim minim veniam,
                nostrud exercitation ullamco laboris nisi ut aliquip ex commodo
                consequat. Duis aute non proident, sunt in culpa qui officia deserunt
                mollit anim id est laborum.
              </p>
            </div>
            <div class="describe-btn">
              <span class="badge bg-warning-light text-warning-light me-2">Low</span>
              <span class="badge badge-gray-outline me-2">#4987</span>
              <span><i class="feather feather-message-square text-gray-light fw-normal me-2"></i>3</span>
            </div>
          </div>
        </div>
        <!-- /card -->
      </div>
      <!-- /Ticket list -->
    </div>
  </div>
  <!-- /Page Wrapper -->
  <ticketmodal></ticketmodal>
</template>
<script>
export default {
  setup() {
    return {
      title: String,
      text: String
    };
  },
};
</script>

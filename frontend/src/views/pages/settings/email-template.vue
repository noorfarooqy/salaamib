<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- /Page Header -->
      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar></settingsidebar>
        </div>
        <div class="col-xl-9 col-md-8">
          <div class="page-header">
            <div class="content-page-header">
              <h5>Email Templates</h5>
              <div class="page-content">
                <div class="list-btn">
                  <ul class="filter-list">
                    <li>
                      <a
                        class="btn btn-primary"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#add_custom"
                        ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add
                        Template</a
                      >
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <!-- /Page Header -->

          <div class="email-template-card">
            <div class="row">
              <div class="col-xl-4 col-md-6 d-flex">
                <div class="card">
                  <div class="card-body">
                    <h5>Email Verification</h5>
                    <div class="d-flex package-edit">
                      <a
                        class="btn-action-icon me-2"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#edit_email"
                        ><i class="feather feather-edit"></i
                      ></a>
                      <a
                        class="btn-action-icon"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#delete_modal"
                        ><i class="feather feather-trash-2"></i
                      ></a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6 d-flex">
                <div class="card">
                  <div class="card-body">
                    <h5>Welcome Email</h5>
                    <div class="d-flex package-edit">
                      <a
                        class="btn-action-icon me-2"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#edit_email"
                        ><i class="feather feather-edit"></i
                      ></a>
                      <a
                        class="btn-action-icon"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#delete_modal"
                        ><i class="feather feather-trash-2"></i
                      ></a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6 d-flex">
                <div class="card">
                  <div class="card-body">
                    <h5>Feature Announcement</h5>
                    <div class="d-flex package-edit">
                      <a
                        class="btn-action-icon me-2"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#edit_email"
                        ><i class="feather feather-edit"></i
                      ></a>
                      <a
                        class="btn-action-icon"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#delete_modal"
                        ><i class="feather feather-trash-2"></i
                      ></a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6 d-flex">
                <div class="card">
                  <div class="card-body">
                    <h5>Plan Announcement</h5>
                    <div class="d-flex package-edit">
                      <a
                        class="btn-action-icon me-2"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#edit_email"
                        ><i class="feather feather-edit"></i
                      ></a>
                      <a
                        class="btn-action-icon"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#delete_modal"
                        ><i class="feather feather-trash-2"></i
                      ></a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6 d-flex">
                <div class="card">
                  <div class="card-body">
                    <h5>Engagement/Usage Reminder</h5>
                    <div class="d-flex package-edit">
                      <a
                        class="btn-action-icon me-2"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#edit_email"
                        ><i class="feather feather-edit"></i
                      ></a>
                      <a
                        class="btn-action-icon"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#delete_modal"
                        ><i class="feather feather-trash-2"></i
                      ></a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6 d-flex">
                <div class="card">
                  <div class="card-body">
                    <h5>Feedback Request</h5>
                    <div class="d-flex package-edit">
                      <a
                        class="btn-action-icon me-2"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#edit_email"
                        ><i class="feather feather-edit"></i
                      ></a>
                      <a
                        class="btn-action-icon"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#delete_modal"
                        ><i class="feather feather-trash-2"></i
                      ></a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6 d-flex">
                <div class="card">
                  <div class="card-body">
                    <h5>Plan Renewal Reminder</h5>
                    <div class="d-flex package-edit">
                      <a
                        class="btn-action-icon me-2"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#edit_email"
                        ><i class="feather feather-edit"></i
                      ></a>
                      <a
                        class="btn-action-icon"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#delete_modal"
                        ><i class="feather feather-trash-2"></i
                      ></a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6 d-flex">
                <div class="card">
                  <div class="card-body">
                    <h5>Plan Expired</h5>
                    <div class="d-flex package-edit">
                      <a
                        class="btn-action-icon me-2"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#edit_email"
                        ><i class="feather feather-edit"></i
                      ></a>
                      <a
                        class="btn-action-icon"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#delete_modal"
                        ><i class="feather feather-trash-2"></i
                      ></a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6 d-flex">
                <div class="card">
                  <div class="card-body">
                    <h5>Policy Update Notice</h5>
                    <div class="d-flex package-edit">
                      <a
                        class="btn-action-icon me-2"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#edit_email"
                        ><i class="feather feather-edit"></i
                      ></a>
                      <a
                        class="btn-action-icon"
                        href="javascript:void(0);"
                        data-bs-toggle="modal"
                        data-bs-target="#delete_modal"
                        ><i class="feather feather-trash-2"></i
                      ></a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Page Wrapper -->
    </div>
  </div>
  <email-template-modal></email-template-modal>
</template>

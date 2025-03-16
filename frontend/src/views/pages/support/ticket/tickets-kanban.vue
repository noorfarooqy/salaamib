<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <ticketheader :title="title" :text="text" />
      <searchfilter />
      <card />
      <tab />
      <!-- Ticket Kanban -->
      <div class="row">
        <div class="col-sm-12">
          <div class="kanban-ticket-main d-flex">
            <ul class="kanban-ticket-list">
              <li class="kanban-ticket-grid">
                <div class="kanban-ticket d-flex justify-content-between align-items-center">
                  <div class="kanban-head css-equal-heights">
                    <h6 class="me-2">Open</h6>
                    <span class="inovices-widget-icon rounded-circle bg-warning-light text-warning-light">5</span>
                  </div>
                  <a href="javascript:;"><span><i class="feather feather-plus"></i></span></a>
                </div>
              </li>
              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-warning-light text-warning-light">Medium</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Support for theme</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-success-light">Resolved</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge badge bg-primary-light">Low</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Verify your email</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-danger-light text-danger-light">Open</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-danger-light">High</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Management</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-light-gray text-secondary">Closed</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-primary-light">Low</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Support for theme</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-success-light">Resolved</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->
            </ul>

            <ul class="kanban-ticket-list">
              <li class="kanban-ticket-grid">
                <div class="kanban-ticket d-flex justify-content-between align-items-center">
                  <div class="kanban-head css-equal-heights">
                    <h6 class="me-2">In Progress</h6>
                    <span class="inovices-widget-icon rounded-circle bg-warning-light text-warning-light">8</span>
                  </div>
                  <a href="javascript:;"><span><i class="feather feather-plus"></i></span></a>
                </div>
              </li>
              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-danger-light">High</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Management</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-danger-light text-danger-light">Open</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge badge bg-primary-light">Low</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Verify your email</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-warning-light text-warning-light">Pending</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-warning-light text-warning-light">Medium</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Support for theme</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-light-gray text-secondary">Closed</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-danger-light">High</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Management</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-warning-light text-warning-light">Pending</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->
            </ul>

            <ul class="kanban-ticket-list">
              <li class="kanban-ticket-grid">
                <div class="kanban-ticket d-flex justify-content-between align-items-center">
                  <div class="kanban-head css-equal-heights">
                    <h6 class="me-2">Hold</h6>
                    <span class="inovices-widget-icon rounded-circle bg-warning-light text-warning-light">6</span>
                  </div>
                  <a href="javascript:;"><span><i class="feather feather-plus"></i></span></a>
                </div>
              </li>
              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-primary-light">Low</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Support for theme</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-light-gray text-secondary">Closed</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-danger-light">High</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Management</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-danger-light text-danger-light">Open</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge badge bg-primary-light">Low</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Verify your email</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-danger-light text-danger-light">Open</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-danger-light">High</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Management</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-warning-light text-warning-light">Pending</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->
            </ul>

            <ul class="kanban-ticket-list">
              <li class="kanban-ticket-grid">
                <div class="kanban-ticket d-flex justify-content-between align-items-center">
                  <div class="kanban-head css-equal-heights">
                    <h6 class="me-2">Unassigned</h6>
                    <span class="inovices-widget-icon rounded-circle bg-warning-light text-warning-light">5</span>
                  </div>
                  <a href="javascript:;"><span><i class="feather feather-plus"></i></span></a>
                </div>
              </li>
              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-primary-light">Low</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Support for theme</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-light-gray text-secondary">Closed</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-danger-light">High</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Management</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-danger-light text-danger-light">Open</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge badge bg-primary-light">Low</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Verify your email</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-danger-light text-danger-light">Open</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-warning-light text-warning-light">Medium</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Support for theme</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-success-light">Resolved</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->
            </ul>

            <ul class="kanban-ticket-list">
              <li class="kanban-ticket-grid">
                <div class="kanban-ticket d-flex justify-content-between align-items-center">
                  <div class="kanban-head css-equal-heights">
                    <h6 class="me-2">Solved</h6>
                    <span class="inovices-widget-icon rounded-circle bg-warning-light text-warning-light">10</span>
                  </div>
                  <a href="javascript:;"><span><i class="feather feather-plus"></i></span></a>
                </div>
              </li>
              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge badge bg-primary-light">Low</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Verify your email</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-danger-light text-danger-light">Open</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-warning-light text-warning-light">Medium</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Support for theme</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-success-light">Resolved</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-danger-light">High</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Management</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-danger-light text-danger-light">Open</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->

              <!-- list Grid -->
              <li class="kanban-ticket-grid">
                <div class="card-kanban">
                  <div class="kanban-box">
                    <div class="kanban-name d-flex justify-content-between align-items-center">
                      <span class="badge bg-primary-light">Low</span>
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="action-icon dropdown-toggle" data-bs-toggle="dropdown"
                          aria-expanded="false"><i class="fas fa-ellipsis-h"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                            data-bs-target="#edit_ticket"><i class="far fa-edit me-2"></i>Edit</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                          <a class="dropdown-item" href="javascript:void(0);"><i
                              class="far fa-trash-alt me-2"></i>Delete</a>
                        </div>
                      </div>
                    </div>
                    <h6>Support for theme</h6>
                    <div class="ticket-due d-flex">
                      <div class="ticket-due-id me-2">
                        <span class="badge badge-gray-outline">#4987</span>
                      </div>
                      <div class="ticket-due-status">
                        <span class="badge bg-success-light">Resolved</span>
                      </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between">
                      <ul class="kanban-ticket-img d-flex align-items-center">
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 1">
                            <img class="avatar-img rounded-circle" src="@/assets/img/profiles/avatar-01.jpg" alt="img" />
                          </a>
                        </li>
                        <li>
                          <a href="javascript:;" data-bs-toggle="tooltip" data-bs-placement="top" title=""
                            data-bs-original-title="Member 2"><img class="avatar-img rounded-circle"
                              src="@/assets/img/profiles/avatar-02.jpg" alt="img" /></a>
                        </li>
                        <li class="more-set">
                          <a href="javascript:;"><span class="d-flex justify-content-center align-items-center"><i
                                class="feather feather-plus"></i></span></a>
                        </li>
                      </ul>
                      <div class="progressset">
                        <p>
                          <span><i class="far fa-calendar me-2"></i></span> Jan 2023
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
              <!-- /list Grid -->
            </ul>
          </div>
        </div>
      </div>
      <!-- /Ticket Kanban -->
    </div>
  </div>
  <!-- /Page Wrapper -->

  <ticketkanban-model></ticketkanban-model>
</template>
<script>
export default {
  setup() {
    return {
      title: "Tickets",
      text: "New Tickets",
    };
  },
};
</script>
